// Backup: Used by Airtable to gather Summary Data

/**
 * Returns a count of all the incomplete 'SPECIFICATION' records.
 * @param {Array} records - The array of records to check.
 * @returns {Promise<number>} - The count of incomplete records.
 */
async function getMissingSpecCount(records) {
  let incomplete = 0;
  for (let record of records) {
    let specValue = record.getCellValue("SPECIFICATION");
    if (specValue === null) {
      incomplete += 1;
    } else {
      if (specValue.name !== "COMPLETE" && specValue.name !== "NA") {
        incomplete += 1;
      }
    }
  }
  return incomplete;
}

/**
 * Returns the count of all the missing/empty 'DATA_SHEET' records.
 * @param {Array} records - The array of records to check.
 * @returns {Promise<number>} - The count of missing/empty 'DATA_SHEET' records.
 */
async function getMissingDatasheetCount(records) {
  let incomplete = 0;
  for (let record of records) {
    if (record.getCellValue("DATA_SHEET") === null) {
      incomplete += 1;
    }
  }
  return incomplete;
}

/**
 * Retrieves the count of missing/incomplete SPECIFICATION and DATA_SHEET records for a given table.
 * @param {string} tableName - The name of the table to retrieve missing values from.
 * @returns {Promise<{ datasheets: number, specifications: number }>} - An object containing the count of missing datasheets and specifications.
 */
async function getMissingValuesForTable(tableName) {
  const table = base.getTable(tableName);
  const query = await table.selectRecordsAsync({
    fields: ["SPECIFICATION", "DATA_SHEET"],
  });
  const specificationsCount = await getMissingSpecCount(query.records);
  const datasheetsCount = await getMissingDatasheetCount(query.records);

  return {
    datasheets: datasheetsCount,
    specifications: specificationsCount,
  };
}

/**
 * Collects summary updates into a single array.
 *
 * @param {Table} tableSummary - The summary table object.
 * @param {Object} newValues - The new values object containing updated values.
 * @returns {Promise<Array>} - An array of replacements.
 */
async function collectSummaryUpdates(tableSummary, newValues) {
  let replacements = [];
  let result = await tableSummary.selectRecordsAsync({
    fields: ["MISSING_SPECS", "MISSING_DATASHEETS"],
  });
  for (let record of result.records) {
    if (newValues[record.name] !== undefined) {
      replacements.push({
        record: record,
        MISSING_SPECS: newValues[record.name].specifications,
        MISSING_DATASHEETS: newValues[record.name].datasheets,
      });
    }
  }
  return replacements;
}

/**
 * Updates the records in the SUMMARY Table with the provided replacements.
 * @param {Table} tableSummary - The SUMMARY Table object.
 * @param {Array} replacements - An array of replacement objects.
 * @returns {Promise<void>} - A promise that resolves when the update is complete.
 */
async function updateSummaryTable(tableSummary, replacements) {
  let fieldMissingSpecs = tableSummary.getField("MISSING_SPECS");
  let fieldDatasheets = tableSummary.getField("MISSING_DATASHEETS");
  if (!replacements.length) {
    output.text("No Update Needed");
  } else {
    // Create the SUMMARY table update records
    let updates = replacements.map((replacement) => ({
      id: replacement.record.id,
      fields: {
        [fieldMissingSpecs.id]: replacement.MISSING_SPECS,
        [fieldDatasheets.id]: replacement.MISSING_DATASHEETS,
      },
    }));

    // Only up to 50 record updates are allowed at one time, so do it in batches
    while (updates.length > 0) {
      await tableSummary.updateRecordsAsync(updates.slice(0, 50));
      updates = updates.slice(50);
    }
  }
}

// ------------------------------------------------------------------------
//-- Collect all the Missing Data from the various Tables
const newValues = {};
newValues.APPLIANCES = await getMissingValuesForTable("APPLIANCES");
newValues.FANS = await getMissingValuesForTable("FANS");
newValues.PUMPS = await getMissingValuesForTable("PUMPS");
newValues.LIGHTING_FIXTURES = await getMissingValuesForTable(
  "LIGHTING FIXTURES"
);
newValues.ERV_UNITS = await getMissingValuesForTable("ERV UNITS");
newValues.MATERIAL_LAYERS = await getMissingValuesForTable("MATERIAL LAYERS");
newValues.GLAZING_TYPES = await getMissingValuesForTable(
  "WINDOW: GLAZING TYPES"
);
newValues.FRAME_TYPES = await getMissingValuesForTable("WINDOW: FRAME TYPES");

// ------------------------------------------------------------------------
//-- Collect any required changes to the 'SUMMARY' table in a single Array
const tableSummary = base.getTable("SUMMARY");
const replacements = await collectSummaryUpdates(tableSummary, newValues);
await updateSummaryTable(tableSummary, replacements);
console.log("Summary Updated");

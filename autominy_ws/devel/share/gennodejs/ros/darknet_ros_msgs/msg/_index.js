
"use strict";

let ObjectCount = require('./ObjectCount.js');
let BoundingBoxes = require('./BoundingBoxes.js');
let BoundingBox = require('./BoundingBox.js');
let CheckForObjectsAction = require('./CheckForObjectsAction.js');
let CheckForObjectsActionFeedback = require('./CheckForObjectsActionFeedback.js');
let CheckForObjectsActionGoal = require('./CheckForObjectsActionGoal.js');
let CheckForObjectsGoal = require('./CheckForObjectsGoal.js');
let CheckForObjectsFeedback = require('./CheckForObjectsFeedback.js');
let CheckForObjectsActionResult = require('./CheckForObjectsActionResult.js');
let CheckForObjectsResult = require('./CheckForObjectsResult.js');

module.exports = {
  ObjectCount: ObjectCount,
  BoundingBoxes: BoundingBoxes,
  BoundingBox: BoundingBox,
  CheckForObjectsAction: CheckForObjectsAction,
  CheckForObjectsActionFeedback: CheckForObjectsActionFeedback,
  CheckForObjectsActionGoal: CheckForObjectsActionGoal,
  CheckForObjectsGoal: CheckForObjectsGoal,
  CheckForObjectsFeedback: CheckForObjectsFeedback,
  CheckForObjectsActionResult: CheckForObjectsActionResult,
  CheckForObjectsResult: CheckForObjectsResult,
};

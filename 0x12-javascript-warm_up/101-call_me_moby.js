#!/usr/bin/node

exports.calMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};

#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const id in dict) {
  const occ = dict[id];
  if (!newDict[occ]) {
    newDict[occ] = [];
  }
  newDict[occ].push(id);
}
console.log(newDict);

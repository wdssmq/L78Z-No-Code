export interface CycleListItem {
  value: number;
}

export interface Stores {
  isRunning: boolean,
  // -------------------
  inpNum: null | number,
  lstNum: null | number,
  swNth: boolean,
  rltMsg: string,
  lstMsg: string,
  // -------------------
  baseNum: Array<number>,
  baseLen: number,
  rltObj: Record<string, number[]>,
  rltList: Array<Array<number | string>>,
  // -------------------
  curDays: number,
  cycleList: Array<CycleListItem>,
  curCycle: number,
  curIndex: number,
}

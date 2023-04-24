(() => {
  const _str = (length) => {
    let str = length.toString();
    str += "丨";
    while (str.length < length) {
      str += String.fromCharCode(Math.floor(Math.random() * 26) + 97);
    }
    return str;
  };
  const fnMain = (input) => {
    const tpl = `echo [InternetShortcut] > "-name-.url"`;
    let bash = '';
    for (let index = input - 5; index < input + 5; index++) {
      // 生成一个字符串长度为 index 的随机字符串
      const str = _str(index);
      // 替换模板中的 -name- 为随机字符串
      bash += `# ${index}\n`;
      bash += tpl.replace('-name-', str) + "\n";
    }
    console.log(bash);
  };
  fnMain(155);
})();

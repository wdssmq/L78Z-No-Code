## Z-BlogASP 插件 fixCommet

当年转换数据时造成了某个问题，写了这个插件来批量修复；

虽然已经忘记是啥问题了，代码要再看懂也会很费事吧；

```sql
UPDATE blog_Comment SET blog_Comment.comm_Content = RTrim(LTrim(blog_Comment.comm_Content));
```

rule auto_rule_20250726192033_9829 {
  strings:
    $o0 = "dword_464288" wide ascii nocase
    $o1 = "_malloc_dbg" wide ascii nocase
  condition:
    all of them
}
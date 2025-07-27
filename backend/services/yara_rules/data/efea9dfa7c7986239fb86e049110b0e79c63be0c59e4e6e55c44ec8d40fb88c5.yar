rule auto_rule_20250726233954_9727 {
  strings:
    $o0 = "dword_4674E0" wide ascii nocase
    $o1 = "dword_467EEC" wide ascii nocase
    $o2 = "_malloc_dbg" wide ascii nocase
  condition:
    3 of ($o*)
}
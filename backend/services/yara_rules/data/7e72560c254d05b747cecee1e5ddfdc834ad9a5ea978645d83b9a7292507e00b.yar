rule auto_rule_20250726203643_9832 {
  strings:
    $o0 = "dword_477104" wide ascii nocase
    $o1 = "__ascii_strnicmp" wide ascii nocase
  condition:
    all of them
}
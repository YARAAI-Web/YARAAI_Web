rule auto_rule_20250726232620_0361 {
  strings:
    $o0 = "dword_475E30" wide ascii nocase
    $o1 = "__ascii_stricmp" wide ascii nocase
    $o2 = "_msize" wide ascii nocase
  condition:
    3 of ($o*)
}
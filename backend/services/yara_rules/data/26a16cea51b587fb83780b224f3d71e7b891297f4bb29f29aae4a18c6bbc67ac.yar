rule auto_rule_20250726132924_7933 {
  strings:
    $o0 = "dword_44E5D8" wide ascii nocase
    $o1 = "__ascii_stricmp" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726074140_6211 {
  strings:
    $o0 = "universal" wide ascii nocase
    $o1 = "dword_10015978" wide ascii nocase
    $o2 = "_realloc_base" wide ascii nocase
  condition:
    3 of ($o*)
}
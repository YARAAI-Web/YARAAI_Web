rule auto_rule_20250726201832_1121 {
  strings:
    $o0 = "FileA" wide ascii nocase
    $o1 = "aClsid" wide ascii nocase
    $o2 = "aProgid" wide ascii nocase
  condition:
    3 of ($o*)
}
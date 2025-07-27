rule auto_rule_20250726184433_1422 {
  strings:
    $o0 = "off_460138" wide ascii nocase
    $o1 = "dword_461B0C" wide ascii nocase
    $o2 = "dword_45FE30" wide ascii nocase
  condition:
    3 of ($o*)
}
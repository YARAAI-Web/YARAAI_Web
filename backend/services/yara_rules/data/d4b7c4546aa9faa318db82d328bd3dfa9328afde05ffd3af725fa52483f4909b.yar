rule auto_rule_20250726190001_7904 {
  strings:
    $o0 = "dword_4C1308" wide ascii nocase
    $o1 = "dword_4C1268" wide ascii nocase
    $o2 = "off_4B186C" wide ascii nocase
  condition:
    3 of ($o*)
}
rule auto_rule_20250726081550_6232 {
  strings:
    $o0 = "dword_45CB04" wide ascii nocase
    $o1 = "dword_45CAF4" wide ascii nocase
    $o2 = "report_failure" wide ascii nocase
    $o3 = "strcat" wide ascii nocase
    $o4 = "differ" wide ascii nocase
  condition:
    4 of ($o*)
}
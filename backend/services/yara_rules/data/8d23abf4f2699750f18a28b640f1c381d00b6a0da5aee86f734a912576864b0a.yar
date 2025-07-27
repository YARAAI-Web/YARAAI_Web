rule auto_rule_20250727014117_3747 {
  strings:
    $o0 = "tail_loop_start" wide ascii nocase
    $o1 = "dword_471ED0" wide ascii nocase
    $o2 = "off_4723A4" wide ascii nocase
    $o3 = "x1004u" wide ascii nocase
    $o4 = "lpCharType" wide ascii nocase
  condition:
    4 of ($o*)
}
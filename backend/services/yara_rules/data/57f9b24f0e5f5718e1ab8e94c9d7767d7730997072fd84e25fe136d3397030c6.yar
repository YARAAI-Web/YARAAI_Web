rule auto_rule_20250727023301_2813 {
  strings:
    $o0 = "kr00_2" wide ascii nocase
    $o1 = "dword_1E5FC" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}
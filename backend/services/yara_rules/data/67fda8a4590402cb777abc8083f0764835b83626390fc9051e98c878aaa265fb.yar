rule auto_rule_20250726151457_6035 {
  strings:
    $o0 = "GetSidSubAuthority" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "dword_45CC18" wide ascii nocase
  condition:
    3 of ($o*)
}
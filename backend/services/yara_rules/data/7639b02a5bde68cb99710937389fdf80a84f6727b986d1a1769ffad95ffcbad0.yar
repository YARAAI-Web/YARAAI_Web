rule auto_rule_20250726183800_7891 {
  strings:
    $o0 = "rgsabound" wide ascii nocase
    $o1 = "dword_1420BEB4" wide ascii nocase
    $o2 = "dword_1420C94C" wide ascii nocase
  condition:
    3 of ($o*)
}
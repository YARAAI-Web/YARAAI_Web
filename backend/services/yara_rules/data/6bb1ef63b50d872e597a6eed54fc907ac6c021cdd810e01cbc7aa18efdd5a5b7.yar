rule auto_rule_20250727030811_1934 {
  strings:
    $o0 = "dword_42273E" wide ascii nocase
    $o1 = "dword_422192" wide ascii nocase
    $o2 = "PathCompactPathExW" wide ascii nocase
  condition:
    3 of ($o*)
}
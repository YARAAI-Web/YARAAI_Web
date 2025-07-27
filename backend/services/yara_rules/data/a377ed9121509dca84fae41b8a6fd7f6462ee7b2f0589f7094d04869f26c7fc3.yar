rule auto_rule_20250726133817_5986 {
  strings:
    $o0 = "dword_42A885" wide ascii nocase
    $o1 = "dword_42A77D" wide ascii nocase
    $o2 = "off_41EB06" wide ascii nocase
    $o3 = "dword_42A7F1" wide ascii nocase
    $o4 = "off_42A891" wide ascii nocase
  condition:
    4 of ($o*)
}
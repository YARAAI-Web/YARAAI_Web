rule auto_rule_20250726202744_6121 {
  strings:
    $o0 = "dwShareMode" wide ascii nocase
    $o1 = "dword_417C94" wide ascii nocase
    $o2 = "off_40251C" wide ascii nocase
    $o3 = "ulOptions" wide ascii nocase
  condition:
    4 of ($o*)
}
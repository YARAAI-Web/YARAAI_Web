rule auto_rule_20250726230303_7014 {
  strings:
    $o0 = "off_40251C" wide ascii nocase
    $o1 = "dword_417C94" wide ascii nocase
  condition:
    all of them
}
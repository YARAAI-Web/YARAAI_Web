rule auto_rule_20250726125015_2252 {
  strings:
    $o0 = "d5m0" wide ascii nocase
    $o1 = "off_4B186C" wide ascii nocase
    $o2 = "UnregisterHotKey" wide ascii nocase
    $o3 = "dword_4C12A4" wide ascii nocase
  condition:
    4 of ($o*)
}
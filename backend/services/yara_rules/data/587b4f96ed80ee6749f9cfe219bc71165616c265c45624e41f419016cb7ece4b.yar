rule auto_rule_20250726121522_8802 {
  strings:
    $o0 = "MessageBoxIndirectW" wide ascii nocase
    $o1 = "CharToOemBuffW" wide ascii nocase
    $o2 = "hData" wide ascii nocase
    $o3 = "crKey" wide ascii nocase
    $o4 = "dwExStyle" wide ascii nocase
  condition:
    4 of ($o*)
}
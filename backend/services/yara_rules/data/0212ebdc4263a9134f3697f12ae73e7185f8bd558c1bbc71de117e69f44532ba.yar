rule auto_rule_20250726204146_4075 {
  strings:
    $o0 = "QtTlsHello" wide ascii nocase
    $o1 = "off_756214" wide ascii nocase
    $o2 = "dword_7560E0" wide ascii nocase
    $o3 = "dword_756308" wide ascii nocase
  condition:
    4 of ($o*)
}
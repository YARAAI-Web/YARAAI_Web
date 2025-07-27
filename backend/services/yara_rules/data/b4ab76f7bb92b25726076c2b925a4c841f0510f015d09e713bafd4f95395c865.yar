rule auto_rule_20250727002903_1442 {
  strings:
    $o0 = "dword_41F887" wide ascii nocase
    $o1 = "DhcpAddServer" wide ascii nocase
  condition:
    all of them
}
rule auto_rule_20250726215946_7122 {
  strings:
    $o0 = "nCode" wide ascii nocase
    $o1 = "hWndNewViewer" wide ascii nocase
    $o2 = "GetWindowTextLengthW" wide ascii nocase
    $o3 = "lpPoint" wide ascii nocase
    $o4 = "TabbedTextOutA" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726215949_0194 {
  strings:
    $o0 = "PaintDesktop" wide ascii nocase
    $o1 = "LoadKeyboardLayoutA" wide ascii nocase
    $o2 = "bRevert" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726215958_1512 {
  condition:
    auto_rule_20250726215946_7122 or auto_rule_20250726215949_0194
}
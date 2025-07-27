rule auto_rule_20250727013958_3622 {
  strings:
    $o0 = "p_hWnd" wide ascii nocase
    $o1 = "_swprintf" wide ascii nocase
    $o2 = "dword_4C1160" wide ascii nocase
    $o3 = "UnregisterHotKey" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250727023112_3305 {
  strings:
    $o0 = "fuLoad" wide ascii nocase
    $o1 = "SendDlgItemMessageA" wide ascii nocase
    $o2 = "SetWindowsHookA" wide ascii nocase
    $o3 = "bRepaint" wide ascii nocase
  condition:
    4 of ($o*)
}
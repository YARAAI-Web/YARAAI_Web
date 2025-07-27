rule auto_rule_20250727040541_6766 {
  strings:
    $o0 = "x15500u" wide ascii nocase
    $o1 = "SendDlgItemMessageA" wide ascii nocase
    $o2 = "SendMessageCallbackA" wide ascii nocase
    $o3 = "lpfnEnum" wide ascii nocase
  condition:
    4 of ($o*)
}
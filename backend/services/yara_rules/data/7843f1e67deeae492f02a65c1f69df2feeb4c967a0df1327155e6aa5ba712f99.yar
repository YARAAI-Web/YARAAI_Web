rule auto_rule_20250727024723_4764 {
  strings:
    $o0 = "ConnectNamedPipe" wide ascii nocase
    $o1 = "GetWindowContextHelpId" wide ascii nocase
    $o2 = "IsBadStringPtrA" wide ascii nocase
    $o3 = "lpCommProp" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726095801_9394 {
  strings:
    $o0 = "CharLowerA" wide ascii nocase
    $o1 = "DestroyCaret" wide ascii nocase
    $o2 = "nIDDlgItem" wide ascii nocase
    $o3 = "IsZoomed" wide ascii nocase
  condition:
    4 of ($o*)
}
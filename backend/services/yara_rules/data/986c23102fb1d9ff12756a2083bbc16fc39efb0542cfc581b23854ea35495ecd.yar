rule auto_rule_20250727040125_2434 {
  strings:
    $o0 = "lpwcx" wide ascii nocase
    $o1 = "flAllocationType" wide ascii nocase
    $o2 = "DestroyCaret" wide ascii nocase
    $o3 = "nIDCheckButton" wide ascii nocase
  condition:
    4 of ($o*)
}
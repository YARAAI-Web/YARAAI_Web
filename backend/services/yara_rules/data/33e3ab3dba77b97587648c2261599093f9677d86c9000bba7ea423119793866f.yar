rule auto_rule_20250726082027_2146 {
  strings:
    $o0 = "SetMenuItemInfoA" wide ascii nocase
    $o1 = "DdeConnectList" wide ascii nocase
    $o2 = "plii" wide ascii nocase
    $o3 = "lpwinsta" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250727013716_2277 {
  strings:
    $o0 = "SetROP2" wide ascii nocase
    $o1 = "nDenominator" wide ascii nocase
    $o2 = "uSize" wide ascii nocase
    $o3 = "GetProfileIntW" wide ascii nocase
    $o4 = "lprcSrc1" wide ascii nocase
  condition:
    5 of ($o*)
}
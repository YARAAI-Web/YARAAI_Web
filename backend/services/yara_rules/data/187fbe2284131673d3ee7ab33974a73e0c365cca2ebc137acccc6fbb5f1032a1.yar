rule auto_rule_20250726230357_0495 {
  strings:
    $o0 = "dword_44A3C4" wide ascii nocase
    $o1 = "x6186" wide ascii nocase
    $o2 = "v233" wide ascii nocase
    $o3 = "x51000C20" wide ascii nocase
  condition:
    4 of ($o*)
}
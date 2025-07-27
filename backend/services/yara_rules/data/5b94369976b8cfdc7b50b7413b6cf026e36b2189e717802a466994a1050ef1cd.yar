rule auto_rule_20250726234049_7122 {
  strings:
    $o0 = "VirtualAllocEx" wide ascii nocase
    $o1 = "uSize" wide ascii nocase
    $o2 = "aGsyst12111cgcr" wide ascii nocase
    $o3 = "a24gop333eya" wide ascii nocase
  condition:
    4 of ($o*)
}
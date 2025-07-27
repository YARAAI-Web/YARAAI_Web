rule auto_rule_20250726135557_8428 {
  strings:
    $o0 = "RegOpenKeyA" wide ascii nocase
    $o1 = "flAllocationType" wide ascii nocase
    $o2 = "lstrcatW" wide ascii nocase
  condition:
    3 of ($o*)
}
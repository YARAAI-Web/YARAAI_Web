rule auto_rule_20250726064835_7541 {
  strings:
    $o0 = "dwFileOffsetHigh" wide ascii nocase
    $o1 = "lptpm" wide ascii nocase
    $o2 = "SetFileApisToANSI" wide ascii nocase
    $o3 = "hMnu" wide ascii nocase
  condition:
    4 of ($o*)
}
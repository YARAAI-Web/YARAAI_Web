rule auto_rule_20250726105621_0436 {
  strings:
    $o0 = "nFilterType" wide ascii nocase
    $o1 = "flProtect" wide ascii nocase
    $o2 = "pdwDefaultLayout" wide ascii nocase
    $o3 = "puiHi" wide ascii nocase
  condition:
    4 of ($o*)
}
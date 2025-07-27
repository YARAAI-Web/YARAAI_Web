rule auto_rule_20250726160630_3891 {
  strings:
    $o0 = "x4923u" wide ascii nocase
    $o1 = "x55D1u" wide ascii nocase
    $o2 = "x3975" wide ascii nocase
    $o3 = "pszFaceName" wide ascii nocase
    $o4 = "xF89C8531" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726164158_4529 {
  strings:
    $o0 = "dwDesiredAccess" wide ascii nocase
    $o1 = "aClsid13709620C" wide ascii nocase
  condition:
    all of them
}
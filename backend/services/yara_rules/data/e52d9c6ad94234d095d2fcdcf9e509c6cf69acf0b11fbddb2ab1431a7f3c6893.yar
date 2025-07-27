rule auto_rule_20250726132028_1430 {
  strings:
    $o0 = "off_44BF64" wide ascii nocase
    $o1 = "InitializeCriticalSec" wide ascii nocase
  condition:
    all of them
}
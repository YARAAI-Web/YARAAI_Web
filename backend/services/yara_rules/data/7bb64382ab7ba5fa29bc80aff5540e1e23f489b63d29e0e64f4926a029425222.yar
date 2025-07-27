rule auto_rule_20250727021935_1922 {
  strings:
    $o0 = "Runtime" wide ascii nocase
    $o1 = "off_44BCA8" wide ascii nocase
    $o2 = "InitializeCriticalSec" wide ascii nocase
  condition:
    3 of ($o*)
}
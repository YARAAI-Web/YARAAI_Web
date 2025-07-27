rule auto_rule_20250726153420_6151 {
  strings:
    $o0 = "dword_45778C" wide ascii nocase
    $o1 = "InitializeCriticalSec" wide ascii nocase
  condition:
    all of them
}
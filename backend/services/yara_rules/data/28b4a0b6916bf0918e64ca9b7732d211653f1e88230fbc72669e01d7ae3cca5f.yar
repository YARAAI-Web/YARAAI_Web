rule auto_rule_20250726155900_7855 {
  strings:
    $o0 = "dword_44BE94" wide ascii nocase
    $o1 = "dword_44C4E0" wide ascii nocase
    $o2 = "InitializeCriticalSec" wide ascii nocase
  condition:
    3 of ($o*)
}
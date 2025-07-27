rule auto_rule_20250726155340_8008 {
  strings:
    $o0 = "dword_472664" wide ascii nocase
    $o1 = "__sbh_alloc_new_group" wide ascii nocase
    $o2 = "InitializeCriticalSec" wide ascii nocase
    $o3 = "dword_471928" wide ascii nocase
    $o4 = "memcpy_0" wide ascii nocase
  condition:
    4 of ($o*)
}
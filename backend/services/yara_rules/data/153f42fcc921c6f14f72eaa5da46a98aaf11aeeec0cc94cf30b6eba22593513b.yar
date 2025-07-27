rule auto_rule_20250726064814_7239 {
  strings:
    $o0 = "GetLocaleInfoA" wide ascii nocase
    $o1 = "dword_451500" wide ascii nocase
    $o2 = "tail_loop_start_0" wide ascii nocase
    $o3 = "InitializeCriticalSec" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250727005827_5770 {
  strings:
    $o0 = "dword_4282FB" wide ascii nocase
    $o1 = "dword_4223DC" wide ascii nocase
    $o2 = "off_42257C" wide ascii nocase
    $o3 = "dword_4282A7" wide ascii nocase
    $o4 = "LockSemaphore" wide ascii nocase
  condition:
    4 of ($o*)
}
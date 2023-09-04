const UIApplication = ObjC.classes.UIApplication;
const sharedApplication = UIApplication.sharedApplication();
const keyWindow = sharedApplication.keyWindow();
const rootViewController = keyWindow.rootViewController();
const mainView = rootViewController.view();

const PTFakeMetaTouch = ObjC.classes.PTFakeMetaTouch;

const simulateTouch = (touchType: number, identifier: number, x: number, y: number) => {
    if(touchType === 0) {
        PTFakeMetaTouch.fakeTouchId_AtPoint_withTouchPhase_inWindow_onView_(identifier, [x, y], 3, keyWindow, mainView);
    } else if(touchType === 1) {
        PTFakeMetaTouch.fakeTouchId_AtPoint_withTouchPhase_inWindow_onView_(identifier, [x, y], 0, keyWindow, mainView);
    } else if(touchType === 2) {
        PTFakeMetaTouch.fakeTouchId_AtPoint_withTouchPhase_inWindow_onView_(identifier, [x, y], 1, keyWindow, mainView);
    }
};

const recvTouch = () => {
    recv("in", (msg) => {
        console.log(msg.ttype, msg.tid, msg.x, msg.y);
        simulateTouch(msg.ttype, msg.tid, msg.x, msg.y);
        recvTouch();
    });
};
recvTouch();
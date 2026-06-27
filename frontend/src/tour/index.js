import { driver } from "driver.js";
import "driver.js/dist/driver.css";

export const createTour = () => {
    const driverObj = driver({
        showProgress: true,
        animate: true,
        allowClose: true,
        doneBtnText: 'Done',
        closeBtnText: 'Skip',
        nextBtnText: 'Next',
        prevBtnText: 'Previous',
        steps: [
            {
                element: '#tour-welcome',
                popover: {
                    title: 'Welcome to Memwyre',
                    description: 'This is your dashboard home for daily AI work.',
                    side: "bottom",
                    align: 'start'
                }
            },
            {
                element: '#tour-timeline',
                popover: {
                    title: 'AI Timeline',
                    description: 'Review and reopen your saved interactions from the timeline panel.',
                    side: "right",
                    align: 'start'
                }
            },
            {
                element: '#tour-quick-actions',
                popover: {
                    title: 'Quick Add',
                    description: 'Capture new ideas, upload documents, or clip web pages instantly.',
                    side: "bottom",
                    align: 'start'
                }
            },
            {
                element: '#tour-inbox',
                popover: {
                    title: 'Inbox',
                    description: 'Review new incoming memories or processing tasks.',
                    side: "bottom",
                    align: 'center'
                }
            },
            {
                element: '#tour-ask',
                popover: {
                    title: 'Ask',
                    description: 'Open Ask to query your saved context and memories.',
                    side: "bottom",
                    align: 'center'
                }
            }
        ]
    });

    return driverObj;
};
